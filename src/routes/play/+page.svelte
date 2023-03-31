<script lang="ts">
	import PlayButton from '../../PlayButton.svelte';
	import Fa from 'svelte-fa';
	import { faPauseCircle, faCog } from '@fortawesome/free-solid-svg-icons';
	import CircleProgressBar from '../../CircleProgressBar.svelte';
	import { onMount } from 'svelte';
	import wordlist from '../../words.json';

	let teamRedScore: number = 0;
	let teamBlueScore: number = 0;
	let currentWord: string;
	let totalSeconds: number = 60.0;
	let currentSeconds: number = totalSeconds;
	let isPaused = false;
	let isPlayer1Turn = true;
	let onBreak = false;

	let breakSeconds = 4;
	let currentBreakSeconds = 4;

	const wordlistLength = wordlist.length;
	function getRandomWord() {
		return wordlist[Math.floor(Math.random() * wordlistLength)];
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
			}
			if (currentSeconds == 0 && !isPaused && !onBreak) {
				// somebody missed a word
				if (isPlayer1Turn) {
					teamRedScore += 1;
				} else {
					teamBlueScore += 1;
				}
				startBreak();
			}
			if (onBreak && currentBreakSeconds > 0 && !isPaused) {
				currentBreakSeconds -= 1;
				currentWord = currentBreakSeconds.toString();
			}
			if (onBreak && currentBreakSeconds == 0) {
				onBreak = false;
				currentBreakSeconds = breakSeconds;
				currentWord = getRandomWord();
				resetTime();
				isPlayer1Turn = !isPlayer1Turn;
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
		<div>
			<Fa icon={faCog} size="3x" color="gray" />
		</div>
	</div>
	<PlayButton
		score={teamBlueScore}
		onClick={p1Click}
		isMyTurn={isPlayer1Turn && !isPaused && !onBreak}
	/>
</div>
