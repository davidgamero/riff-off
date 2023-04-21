<script>
	import '../app.css';
</script>

<div class="dark:bg-gray-900 h-screen">
	<div class="max-w-md mx-auto h-screen p-4">
		<slot />
	</div>
</div>

<style>
	@supports (-webkit-touch-callout: none) {
		.h-screen {
			height: -webkit-fill-available;
		}
	}
</style>
