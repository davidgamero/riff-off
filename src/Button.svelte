<script lang="ts">
	export let text: string;
	export let link: string;
</script>

<a href={link} class="w-full mt-6">
	<div
		class="w-full rounded-md bg-blue-500 my-2 py-6 text-center text-xl text-white dark:text-gray-200"
	>
		<p>{text}</p>
	</div>
</a>
