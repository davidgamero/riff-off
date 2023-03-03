<script lang="ts">
    export let text: string;
    export let link: string;
</script>

<a href={link} class="w-full rounded-md bg-green-500 my-2 py-6 text-center text-white text-xl">
    <p class="">{text}</p>
</a>