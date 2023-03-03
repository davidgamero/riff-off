<script lang="ts">
	export let flipped: boolean = false;
</script>

<div class="bg-red-500 p-10">
	<h1 class:upsidedown={flipped} class="text-center">Got a Word!</h1>
</div>

<style>
	.upsidedown {
		transform: scale(-1, -1);
	}
</style>
