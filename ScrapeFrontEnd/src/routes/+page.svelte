<h1>Welcome to SvelteKit</h1>
<p>{p} <a href="https://kit.svelte.dev">kit.svelte.dev</a> to read the documentation</p>


<script>
let p  = 4;
p = 2;

let src = './South Spirits.png';
import Ghost from './South Spirits.png';

</script>

<img src = {Ghost} alt = "Three ghosts">
<!-- alt= "Three gravestones with ghosts behind them and the compass symbol S on the front grave"-->

<style>

</style>