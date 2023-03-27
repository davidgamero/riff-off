<script lang="ts">
	import PlayButton from '../../PlayButton.svelte';
	import Fa from 'svelte-fa';
	import { faPauseCircle, faCog } from '@fortawesome/free-solid-svg-icons';
	import CircleProgressBar from '../../CircleProgressBar.svelte';
	import { tweened } from 'svelte/motion';
	import Button from '../../Button.svelte';
	import { onMount } from 'svelte';

	let teamRedScore: number;
	let teamBlueScore: number;
	let currentWord: string;
	let totalSeconds: number = 60.0;
	let currentSeconds: number = 60.0;
	let paused = true;

	$: progress = (currentSeconds * 1.0) / totalSeconds;
	function togglePause() {
		console.log('paused' + paused);
		paused = !paused;
	}
	function resetTime() {
		currentSeconds = totalSeconds;
	}

	onMount(() => {
		setInterval(() => {
			console.log(currentSeconds + ' progress:' + progress);
			if (!paused && currentSeconds > 0) {
				currentSeconds -= 1;
			}
		}, 1000);
	});
</script>

<div class="h-full flex flex-col justify-between align-middle p-6">
	<PlayButton flipped={true} bind:score={teamRedScore} />
	<div class="flex justify-between items-center m-4">
		<div on:click={togglePause}>
			<Fa icon={faPauseCircle} size="3x" color="gray" />
		</div>
		<div on:click={resetTime}>
			<CircleProgressBar
				{progress}
				score1={teamBlueScore}
				score2={teamRedScore}
				timeSeconds={currentSeconds}
			/>
		</div>
		<div>
			<Fa icon={faCog} size="3x" color="gray" />
		</div>
	</div>
	<PlayButton bind:score={teamBlueScore} />
</div>
