<script>
    let p =4;
    import ImportMe from './importMe.svelte'; 
    let was = "<strong>  wass up </strong>";
    let string = "need to html the next bit <strong> something</strong>" + {was};

    let count = $state(0);


</script>


<h1>Welcome to SvelteKit</h1>
<p>{p} <a href="https://kit.svelte.dev">kit.svelte.dev</a> to read the documentation</p>
<ImportMe /> <!--looks like it must be capital-->

{@html string} <!--@html tells it to double check for htmls-->
<!--html does not sanatize string, so if someone else is entering it, then it could break everything: do escape yourself-->


<button >
    Clicked {count}
    {count === 1 ? 'time' : 'times'}
</button>


<!--
<script>
let p  = 4;
p = 2;

let src = './South Spirits.png';
import Ghost from './South Spirits.png';
</script>

<img src = {Ghost} alt = "Three ghosts">
-->
<!-- alt= "Three gravestones with ghosts behind them and the compass symbol S on the front grave"-->
