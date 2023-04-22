<script lang='ts'>
    export let score: number;
    export let id: string;
    export let color: string;
</script>


<div>
    <label for={id} class="block mb-2 text-sm font-medium  text-gray-800 dark:text-gray-200">Edit Team {color} Score</label>
    <input type="number" {id} class="bg-white border border-gray-200 text-gray-500 text-sm rounded-lg focus:border-blue-600 block w-4/5 p-2 dark:bg-gray-700 dark:border-gray-700 dark:text-gray-400 dark:focus:text-blue-500 dark:focus:border-blue-500 dark:focus:bg-gray-700" bind:value={score}>
</div>
