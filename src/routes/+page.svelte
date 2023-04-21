<script lang="ts">
	import Button from '../Button.svelte';
	import Settings from '../Settings.svelte';

	let goal: string;
	let duration: string;
	let difficulty: string;
</script>

<div class="flex h-full flex-col items-center justify-center py-2">
	<h2 class="font-pacifico text-2xl font-bold dark:text-gray-300 mb-5">Welcome to</h2>
	<h1 class="font-pacifico text-6xl font-bold dark:text-blue-500 mb-8">Riff Off!</h1>

	<Settings
		bind:selectedGoal={goal}
		bind:selectedDuration={duration}
		bind:selectedDifficulty={difficulty}
	/>
	<Button
		link="/play?duration={duration}&difficulty={difficulty}&goal={goal}"
		text="Start a new game"
	/>
</div>
