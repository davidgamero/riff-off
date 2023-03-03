<script>
	import Button from '../Button.svelte';
	import Settings from '../Settings.svelte';
</script>

<div class="flex min-h-screen flex-col items-center justify-center py-2">
	<h1 class="text-4xl font-bold">Welcome to Riff Off!</h1>

	<Settings />
	<Button link="/play" text="Start a new game" />
</div>
