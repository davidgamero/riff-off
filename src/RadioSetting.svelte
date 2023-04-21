<script lang="ts">
	export let name: string;
	export let values: string[];
	export let selected: string = values[0];
</script>

<div>
	<h2 class="text-center dark:text-gray-300 text-xl mb-2">{name}</h2>
	<div class="flex justify-around">
		{#each values as value}
			<li class="grow">
				<input type="radio" id={value} {name} {value} bind:group={selected} class="hidden peer" />
				<label
					for={value}
					class="inline-flex items-center justify-between w-full p-5 text-gray-500 bg-white border border-gray-200 rounded-lg cursor-pointer dark:hover:text-gray-300 dark:border-gray-700 dark:peer-checked:text-blue-500 peer-checked:border-blue-600 peer-checked:text-blue-600 hover:text-gray-600 hover:bg-gray-100 dark:text-gray-400 dark:bg-gray-800 dark:hover:bg-gray-700"
				>
					<div class="block">
						<div class="w-full text-lg font-semibold">{value}</div>
					</div>
				</label>
			</li>
		{/each}
	</div>
</div>
