<script lang="ts">
	export let text: string;
	export let link: string;
</script>

<a href={link} class="w-full rounded-md bg-blue-500 my-2 py-6 text-center text-xl">
	<p>{text}</p>
</a>
