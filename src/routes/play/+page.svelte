<script lang="ts">
	import PlayButton from '../../PlayButton.svelte';

	let currentWord: string;
</script>

<div class="h-full flex flex-col justify-between align-middle">
	<PlayButton flipped={true} />
	<PlayButton />
</div>
