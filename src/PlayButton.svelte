<script lang="ts">
	export let flipped: boolean = false;
	export let onClick: () => void;
	export let score: number = 0;
	export let isMyTurn: boolean = false;
	const btnColor = flipped ? 'bg-red-500 hover:bg-red-600' : 'bg-blue-500 hover:bg-blue-600';
	const start: string = 'Got a Song!';
</script>

<button
	on:click={onClick}
	class="p-10 rounded-md {isMyTurn ? btnColor : 'bg-gray-400 dark:bg-gray-600'}"
>
	<h1 class:upsidedown={flipped} class="text-center text-white text-2xl ">
		{#if score > 0}
			{score}
		{:else}
			{start}
		{/if}
	</h1>
</button>

<style>
	.upsidedown {
		transform: scale(-1, -1);
	}
</style>
