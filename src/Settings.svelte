<script lang="ts">
	import RadioSetting from './RadioSetting.svelte';
    import Button from './Button.svelte';

	let selectedDifficulty: string;
	let selectedDuration: string;
	let selectedGoal: string;
</script>

<ul class="grid w-full gap-6 md:grid-cols-2">
	<p>Selected Difficulty = {selectedDifficulty}</p>
	<p>Selected Duration = {selectedDuration}</p>
	<p>Selected Goal = {selectedGoal}</p>
	<RadioSetting
		name="Difficulty"
		values={['Easy', 'Medium', 'Hard']}
		bind:selected={selectedDifficulty}
	/>
	<RadioSetting name="Duration" values={['30s', '60s', '90s']} bind:selected={selectedDuration} />
	<RadioSetting name="Goal" values={['5', '10', '15']} bind:selected={selectedGoal} />
</ul>
<Button link="/play" text="Start a new game" />
