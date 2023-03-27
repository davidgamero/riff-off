<script lang="ts">
	// from https://svelte.dev/repl/f1437286b08d4890b9207180868ee37e?version=3.46.4
	export let progress: number;
	export let timeSeconds: number;
	export let score1: number;
	export let score2: number;

	$: angle = 360 * progress;

	// Adapt the logic according to the approach
	$: background = `radial-gradient(white 50%, transparent 51%),
    conic-gradient(transparent 0deg ${angle}deg, gainsboro ${angle}deg 360deg),
    conic-gradient(red 0deg, blue);`;

	$: cssVarStyles = `--background:${background}`;
</script>

<div
	id="progress-circle"
	class="flex flex-col justify-center text-center m-auto"
	style={cssVarStyles}
>
	<h2>Time: {timeSeconds}</h2>
	<h2>Score: {score1}: {score2}</h2>
</div>

<style>
	#progress-circle {
		background: var(--background);
		border-radius: 50%;
		width: 200px;
		height: 200px;
		will-change: transform;
		transition: all 500ms ease-in;
	}
</style>
