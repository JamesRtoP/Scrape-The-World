
<script>
    

    function fetchMeals()
    {
        fetch('./mealsToday.jason')
            .then(response=> {
                if(!response.ok){
                    throw new Error(`Some Shit is fucked 1! Status: ${response.status} `);

                }
                return response.json();
            })
            .then(data=> console.log(data))
            .catch(error=> console.error('Failed to fetch data:', error))
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
    function getSouthsideMenu()
    {
        let something = document.getElementById("southside");

    }
    import mealsToday from '../mealsToday.json';
    Object.keys( mealsToday);

    let JSONmeals = mealsToday
    let entries = Object.entries(JSONmeals)
    //cafe string will not be sanitized, so this is an issue
    let cafeString = "";
    for (let meal in JSONmeals)
    {
        cafeString += `<div class = "food-station"> ${meal} </div>`;
        for (let station in JSONmeals[meal])
        {   
            cafeString += "<br>Station: "+JSONmeals[meal][station]["station"] + "<br>";
            for(let menuItemIndex in JSONmeals[meal][station]["menuItems"])
            {
                cafeString += JSONmeals[meal][station]["menuItems"][menuItemIndex][0]+ "<br>"
            }
            //cafeString += JSONmeals[meal][station]["menuItems"][0]+ "<br>";
        }
        // for (let something in mealsToday[station])
        // {
        //     cafeString += something;
        // }
    }
    //console.log(typeof mealsToday["Breakfast"]);
    //let something = document.getElementsByClassName("cafe-menu");
    for (let index in Object.keys(mealsToday))
    {

    }
    //southsideMenu.innerHTML = cafeString;
    

    
    
</script>

<!--
 

-->


{@html cafeString}

<!-- {@html string} @html tells it to double check for htmls -->
<!--html does not sanatize string, so if someone else is entering it, then it could break everything: do escape yourself-->

<button onclick = {openAllDetails} type = "button"> Open </button>
<button onclick = {closeAllDetails} type = "button"> Close </button>


<article class = c-wrapper>
    <details>
        <summary class = "cafe-building">Southside Cafe</summary>
        <div class = "cafe-menu" id= "southside">
            
            
        </div>

    </details>
    <details>
        <summary class = "cafe-building">Southside Cafe</summary>
        <div class = "cafe-menu">
            {JSON.stringify(mealsToday)}
        </div>

    </details>
    <details>
        <summary class = "cafe-building">Southside Cafe</summary>
        <div class = "cafe-menu">
            {#each mealsToday as thing}
            <h1>{thing}</h1>
        {/each}
        {#each entries as meal}
            {#each meal as mealthing,i}
                {#if i==0}
                    {mealthing}
                    <br>
                {:else}
                    {#each mealthing as station, i}
                        {#if i==1}
                        {JSON.stringify(station)}
                        {/if} 
                    {/each}
                {/if} 
            {/each}
            <br>
            <br>

        {/each}        </div>

    </details>
</article>


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
    .food-station
    {
        font-size:1vh
    }
    
</style>