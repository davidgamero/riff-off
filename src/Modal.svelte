<script lang="ts">
	import { faHome, faWindowClose } from '@fortawesome/free-solid-svg-icons';
	import Fa from 'svelte-fa';

	export let showModal: boolean;
	// export let newGoal: string;
	// export let newDifficulty: string;
	// export let newDuration: string;

	let dialog: HTMLDialogElement; // HTMLDialogElement

	$: if (dialog && showModal) dialog.showModal();
</script>

<!-- svelte-ignore a11y-click-events-have-key-events -->
<dialog
	bind:this={dialog}
	on:close={() => (showModal = false)}
	on:click|self={() => dialog.close()}
>
	<div on:click|stopPropagation>
		<slot name="header" />
		<!-- svelte-ignore a11y-autofocus -->
		<button autofocus on:click={() => dialog.close()}>
			<Fa icon={faWindowClose} size="2x" color="blue" />
		</button>
		<slot />
		<hr />
		<button
			on:click={() => dialog.close()}
			class="block text-center font-pacifico w-full my-4 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
		>
			Submit
		</button>
		<a
			href="/"
			class="block flex justify-center font-pacifico w-full my-4 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
		>
			<Fa icon={faHome} size="1x" color="white" />
		</a>
	</div>
</dialog>

<style>
	dialog {
		max-width: 32em;
		border-radius: 0.2em;
		border: none;
		padding: 0;
	}
	dialog::backdrop {
		background: rgba(0, 0, 0, 0.3);
	}
	dialog > div {
		padding: 1em;
	}
	dialog[open] {
		animation: zoom 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
	}
	@keyframes zoom {
		from {
			transform: scale(0.95);
		}
		to {
			transform: scale(1);
		}
	}
	dialog[open]::backdrop {
		animation: fade 0.2s ease-out;
	}
	@keyframes fade {
		from {
			opacity: 0;
		}
		to {
			opacity: 1;
		}
	}
	button {
		display: block;
	}
</style>
