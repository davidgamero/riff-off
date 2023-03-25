<script lang="ts">
	import PlayButton from '../../PlayButton.svelte';
	import Fa from 'svelte-fa';
	import { faPauseCircle, faCog } from '@fortawesome/free-solid-svg-icons';

	let teamRedScore: number;
	let teamBlueScore: number;
	let currentWord: string;
</script>

<div class="h-full flex flex-col justify-between align-middle p-6">
	<PlayButton flipped={true} bind:score={teamRedScore} />
	<div class="flex justify-between items-center m-4">
		<div>
			<Fa icon={faPauseCircle} size="3x" color="gray" />
		</div>
		<div>
			<h1>Timer{teamBlueScore} {teamRedScore}</h1>
		</div>
		<div>
			<Fa icon={faCog} size="3x" color="gray" />
		</div>
	</div>
	<PlayButton bind:score={teamBlueScore} />
</div>
