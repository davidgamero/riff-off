<script lang="ts">
	export let flipped: boolean = false;
	export let score: number = 0;
	const start: string = 'Got a Song!';
	function handleClick() {
		console.log('clicked');
		score++;
	}
</script>

<div class="bg-red-500 p-10 rounded-md">
	<h1 on:click={handleClick} class:upsidedown={flipped} class="text-center text-white text-2xl">
		{#if score > 0}
			{score}
		{:else}
			{start}
		{/if}
	</h1>
</div>

<style>
	.upsidedown {
		transform: scale(-1, -1);
	}
</style>
