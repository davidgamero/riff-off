<script lang="ts">
	import PlayButton from '../../PlayButton.svelte';

	let currentWord: string;
</script>

<div class="h-full flex flex-col justify-between align-middle p-6">
	<PlayButton flipped={true} />
	<div class="flex justify-between">
		<div>
		 <h1> Pause</h1>
		</div>
		<div>
		 <h1> Timer</h1>
		</div>
		<div>
		 <h1> Settings</h1>
		</div>
	</div>
	<PlayButton />
</div>
