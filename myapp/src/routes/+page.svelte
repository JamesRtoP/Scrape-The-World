
<script>

    
    let p =4;
    let was = "<strong>  wass up </strong>";
    let string = "need to html the next bit <strong> something</strong>" + {was};

    let fives = $state([5])
    function fiven()
    {
        fives.push(fives.at(0))
    }
    let fived = $derived(fives.reduce((t,n) => t*n,1))

    let addy = $state([1,2,3])
    function addyey()
    {
        addy.push(addy.length + 1)
    }

    let count = $state(0);
    let total = $derived(addy.reduce((t,n) => t + n, 0))
    function increment() {
        count++;
		// TODO implement
	}

</script>


<!--CSS Here-->
<style>

</style>

{@html string} <!--@html tells it to double check for htmls-->
<!--html does not sanatize string, so if someone else is entering it, then it could break everything: do escape yourself-->

<br>
<button onclick={increment}>
    Clicked {count}
    {count === 1 ? 'time' : 'times'}
</button>

<br>
<button onclick={addyey}>
    AddSome 
</button>
<p1> {addy.join ( ' + ')} = {total} </p1>

<br>
<button onclick={fiven}>
    Five 
</button>
<p1> {fives.join ( ' * ')} = {fived} </p1>

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
