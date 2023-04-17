<script lang="ts">
	import RadioSetting from './RadioSetting.svelte';
	import { page } from '$app/stores';

	export let selectedDifficulty: string;
	export let selectedDuration: string;
	let selectedGoal: string = '5';
	export let goal: number;
	$: goal = Number(selectedGoal);
	$: goal,
		(function () {
			$page.url.searchParams.set('goal', goal.toString());
		})();
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
