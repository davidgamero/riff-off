<script lang="ts">
	import RadioSetting from './RadioSetting.svelte';

	export let selectedDifficulty: string;
	export let selectedDuration: string;
	export let selectedGoal: string;
</script>

<ul class="grid w-full gap-6 md:grid-cols-1">
	<RadioSetting
		name="Difficulty"
		values={['Easy', 'Medium', 'Hard']}
		bind:selected={selectedDifficulty}
	/>
	<RadioSetting name="Duration" values={['30s', '60s', '90s']} bind:selected={selectedDuration} />
	<RadioSetting name="Goal" values={['5', '10', '15']} bind:selected={selectedGoal} />
</ul>
