
<script>
    
    let was = "<strong>  wass up </strong>";
    let string = "need to html the next bit <strong> something</strong>" + {was};

    let fives = $state([5])
    function fiven()
    {
        fives.push(fives.at(0))
        console.log("ass")

    }
    let fived = $derived(fives.reduce((t,n) => t*n,1))

    let N = $state(0)
    let oOfOneTotal = 2
    let oOfLogN = $derived(Math.log(N)/Math.log(2))
    let oOfNTotal = $derived(2*N)
    let oOfNLogN = $derived(N*(Math.log(N)/Math.log(2)))
    let oOfNSquaredTotal = $derived(N**2)
    let oOfNPowTotal = $derived(2**N)


    console.log("butt")

    function goingCrazy()
    {
        console.log("hello")
    }

    function openAllDetails()
    {
        let elm = document.getElementsByTagName("details");
        for (let i =0; i < elm.length; i++)
        {
            elm[i].open = true;
        }

    }
    function closeAllDetails()
    {
        let elm = document.getElementsByTagName("details");
        for (let i =0; i < elm.length; i++)
        {
            elm[i].removeAttribute("open");
        }
    }

</script>

<!--
 

-->


<!--CSS Here-->
<style>
    .c-wrapper
    {
        display:grid;
        grid-template-columns: 1fr 1fr 1fr;
        column-gap: 2vw;
    }
    [class *= "cafe"]
    {
        text-align: center;
        width: 100%;
    }
    details summary
    {
        font-size:3.5vw;
        border: .5px solid lightgray;
        border-bottom: 2px solid black;
        list-style-type: '';
    }

    details summary:hover
    {
        opacity: 50%;
        cursor:pointer;
    }
    details 
    {
        font-size:2vw;

    }

    

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


<br>

<button onclick = {openAllDetails} type = "button"> Open </button>
<button onclick = {closeAllDetails} type = "button"> Close </button>



<article class = c-wrapper>
    <details>
        <summary class = "cafe-building">Southside Cafe</summary>
        <div class = "cafe-menu">
            Slop for breakfast
            <br>
            slop for dinner
        </div>

    </details>
    <details>
        <summary class = "cafe-building">Southside Cafe</summary>
        <div class = "cafe-menu">
            Slop for breakfast
            <br>
            slop for dinner
        </div>

    </details>
    <details>
        <summary class = "cafe-building">Southside Cafe</summary>
        <div class = "cafe-menu">
            Slop for breakfast
            <br>
            slop for dinner
        </div>

    </details>
</article>
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
