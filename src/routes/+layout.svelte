<script>
	import '../app.css';
</script>

<div class="dark:bg-gray-900">
	<div class="max-w-md mx-auto h-screen ">
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
