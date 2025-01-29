
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


    let N = $state(0)
    let oOfOneTotal = 2
    let oOfLogN = $derived(Math.log(N)/Math.log(2))
    let oOfNTotal = $derived(2*N)
    let oOfNLogN = $derived(N*(Math.log(N)/Math.log(2)))
    let oOfNSquaredTotal = $derived(N**2)
    let oOfNPowTotal = $derived(2**N)

</script>


<!--CSS Here-->
<style>

</style>

{@html string} <!--@html tells it to double check for htmls-->
<!--html does not sanatize string, so if someone else is entering it, then it could break everything: do escape yourself-->

<br>
<button onclick={fiven}>
    Five 
</button>
<p1> {fives.join ( ' * ')} = {fived} </p1>

<br>
<button onclick={N++}>
N = {N}
</button>
<br>
O(1) = {oOfOneTotal}
<br>
O(log N) = {oOfLogN}
<br>
O(N) = {oOfNTotal}
<br>
O(N log N) = {oOfNLogN}
<br>
O(N^2) = {oOfNSquaredTotal}
<br>
O(2^N) = {oOfNPowTotal}
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
