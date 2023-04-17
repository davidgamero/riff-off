<script lang="ts">
	import { page } from '$app/stores';
	import { onMount } from 'svelte';
	import * as confetti from 'canvas-confetti';
	import Button from '../../Button.svelte';

	const winner: string = $page.url.searchParams.get('winner') || 'no-winner';
	let color = winner;

	let isReadyToPlay: string = 'invisible';
	let shouldDisappear: string;

	let myConfetti: confetti.CreateTypes;
	onMount(() => {
		let myCanvas: HTMLCanvasElement = document.getElementById('canvas');
		if (myCanvas !== null) {
			myConfetti = confetti.create(myCanvas, {
				resize: true,
				useWorker: true
			});
		}

		setConfettiIntervals(1000, 5);
	});

	function setConfettiIntervals(delay, repetitions) {
		let confettiBursts: number = 0;
		let intervalID = setInterval(() => {
			console.log(confettiBursts);

			myConfetti({
				particleCount: 300,
				spread: 160,
				origin: {
					x: Math.random(),
					y: Math.random() - 0.2
				}
			});

			if (confettiBursts >= repetitions) {
				window.clearInterval(intervalID);
				isReadyToPlay = 'visible';
				shouldDisappear = 'invisible';
				return;
			}

			confettiBursts++;
		}, delay);
	}

	// onMount(() => {
	//     setConfettiIntervals(1000, 3);

	// });
</script>

<canvas class={shouldDisappear} id="canvas" />
<div class="flex flex-col justify-center align-middle h-full">
	<h1
		class:text-blue-400={color == 'blue'}
		class:text-red-400={color == 'red'}
		class="font-pacifico text-center underline decoration-{color}-400 text-6xl"
	>
		{winner} wins!
	</h1>
	<a
		href="/"
		class="{isReadyToPlay} block text-center font-pacifico w-full my-32 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
	>
		Play Again?
	</a>
</div>

<style>
	#canvas {
		position: fixed;
		left: 0;
		top: 0;
		width: 100%;
		height: 100%;
	}
</style>
