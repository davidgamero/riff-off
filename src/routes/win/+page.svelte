<script lang='ts'>
    import {page} from '$app/stores'
    const winner: string = $page.url.searchParams.get('winner')
</script>

<div>
    <h1>{winner} wins!</h1>
</div>