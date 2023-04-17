<script lang="ts">
	// from https://svelte.dev/repl/f1437286b08d4890b9207180868ee37e?version=3.46.4
	export let progress: number;
	export let timeSeconds: number;
	export let score1: number;
	export let score2: number;
	export let currentWord: string;
	export let isPlayer1Turn: boolean;

	const player1Color = '#dc2626';
	const player2Color = '#3b82f6';
	$: [firstColor, secondColor] = ((colors) => (isPlayer1Turn ? colors : colors.reverse()))([
		player1Color,
		player2Color
	]);

	$: angle = 360 * progress;

	// Adapt the logic according to the approach
	$: background = `radial-gradient(white 50%, transparent 51%),
    conic-gradient(transparent 0deg ${angle}deg, gainsboro ${angle}deg 360deg),
    conic-gradient(${firstColor}, 100grad, ${secondColor});`;

	$: cssVarStyles = `--background:${background}`;
</script>

<div
	id="progress-circle"
	class="flex flex-col justify-center text-center p-10"
	style={cssVarStyles}
>
	<h2 class="pt-3 border-t-2 border-gray-600" style="transform: scale(-1, -1)">{currentWord}</h2>
	<h2 class="mt-3">{currentWord}</h2>
</div>

<style>
	#progress-circle {
		background: var(--background);
		border-radius: 50%;
		width: 200px;
		height: 200px;
		will-change: transform;
		transition: all 1000ms ease-in;
	}
</style>
