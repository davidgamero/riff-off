<script lang="ts">
	import PlayButton from '../../PlayButton.svelte';
	import Fa from 'svelte-fa';
	import { faPauseCircle, faCog } from '@fortawesome/free-solid-svg-icons';
	import CircleProgressBar from '../../CircleProgressBar.svelte';
	import {getWordsFromStorage, recordWordToStorage} from '../../WordLog.svelte';
	import { onMount } from 'svelte';
	import wordlist from '../../words.json';
	import Settings from '../../Settings.svelte';
	import Modal from '../../Modal.svelte';
	import {page} from '$app/stores'
	import {goto} from '$app/navigation'

	let teamRedScore: number = 0;
	let teamBlueScore: number = 0;
	let currentWord: string;
	const totalSeconds: number = parseFloat($page.url.searchParams.get('duration'))
	let currentSeconds: number = totalSeconds;
	let isPaused = false;
	let isPlayer1Turn = true;
	let onBreak = false;
	let newGoal: string;
	let newDuration: string;
	let newDifficulty: string;

	let breakSeconds = 4;
	let currentBreakSeconds = 4;
	
	const goal: number = Number($page.url.searchParams.get('goal'))
	
	let showModal: boolean = false;
	function showSettingsModal() {
		console.log('clicked');
		showModal = true;
	}
	
	function getRandomWord() {
		let localStorageList: string = getWordsFromStorage();
		let filteredWordList: string[] = wordlist.filter((w)=> !localStorageList.includes(w))
		let word: string = filteredWordList[Math.floor(Math.random() * filteredWordList.length)];
		recordWordToStorage(word, 5)
		return word
	}

	$: progress = (currentSeconds * 1.0) / totalSeconds;
	function togglePause() {
		isPaused = !isPaused;
	}

	function resetTime() {
		currentSeconds = totalSeconds;
	}

	function startBreak() {
		onBreak = true;
	}

	onMount(() => {
		currentWord = getRandomWord();
		setInterval(() => {
			if (!isPaused && !onBreak && currentSeconds > 0) {
				currentSeconds -= 1;
			return
			}
			if (currentSeconds == 0 && !isPaused && !onBreak) {
				// somebody missed a word
				if (isPlayer1Turn) {
					teamRedScore += 1;
					if (teamRedScore == goal) {
						// victory screen
						goto("/win?winner=red")
					}
				} else {
					teamBlueScore += 1;
					if (teamBlueScore == goal) {
						//victory screen
						goto("/win?winner=blue")
					}
				}
				startBreak();
				return
			}
			if (onBreak && currentBreakSeconds > 0 && !isPaused) {
				currentBreakSeconds -= 1;
				currentWord = currentBreakSeconds.toString();
				return
			}
			if (onBreak && currentBreakSeconds == 0) {
				onBreak = false;
				currentBreakSeconds = breakSeconds;
				currentWord = getRandomWord();
				resetTime();
				isPlayer1Turn = !isPlayer1Turn;
				return
			}
		}, 1000);
	});

	function p1Click() {
		if (isPlayer1Turn && !onBreak && !isPaused) {
			resetTime();
			isPlayer1Turn = false;
		}
	}
	function p2Click() {
		if (!isPlayer1Turn && !onBreak && !isPaused) {
			resetTime();
			isPlayer1Turn = true;
		}
	}
</script>

<div class="h-full flex flex-col justify-between align-middle p-6">
	<PlayButton
		flipped={true}
		score={teamRedScore}
		onClick={p2Click}
		isMyTurn={!isPlayer1Turn && !isPaused && !onBreak}
	/>
	<div class="flex justify-between items-center m-4">
		<button on:click={togglePause}>
			<Fa icon={faPauseCircle} size="3x" color="gray" />
		</button>
		<button on:click={resetTime}>
			<CircleProgressBar
				{progress}
				{currentWord}
				score1={teamBlueScore}
				score2={teamRedScore}
				timeSeconds={currentSeconds}
			/>
		</button>
		<button on:click={showSettingsModal}>
			<Fa icon={faCog} size="3x" color="gray" />
		</button>
	</div>
	<PlayButton
		score={teamBlueScore}
		onClick={p1Click}
		isMyTurn={isPlayer1Turn && !isPaused && !onBreak}
	/>
</div>

<Modal bind:newGoal={newGoal} bind:newDuration={newDuration} bind:newDifficulty={newDifficulty} bind:showModal>
    <Settings bind:selectedGoal={newGoal} bind:selectedDuration={newDuration} bind:selectedDifficulty={newDifficulty}/>
</Modal>