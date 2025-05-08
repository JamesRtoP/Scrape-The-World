
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
    function convertMealtypeToIcon(mealtype)
    {
        switch(mealtype)
        {
            case "Vegetarian":
                return "<img src = \"/foodIcons/Vegetarian.png\" alt = \"Vegitarian Icon\" class = \"food-icon\" title = \"Vegetarian Item\">"
            break;

            case "Vegan":
                return "<img src = \"/foodIcons/Vegan.png\" alt = \"Vegan Icon\" class = \"food-icon\" title = \"Vegan Item\">"
            break;

            case "Halal":
                return "<img src = \"/foodIcons/Halal.png\" alt = \"Halal Icon\" class = \"food-icon\" title = \"Halal Item\">"
            break;

            case "Healthy Option":
                return "<img src = \"/foodIcons/Healthy Option.png\" alt = \"Healthy Option Icon\" class = \"food-icon\" title = \"Healthy Option item\" style = \"width:3.6vw\">"
            break;

            case "Gluten Friendly":
                return "<img src = \"/foodIcons/Gluten Friendly.png\" alt = \"Gluten Friendly Icon\" class = \"food-icon\" title = \"Gluten Friendly item\" style = \"width:3.6vw\">"
            break;

            case "Allergen-Friendly":
                return "<img src = \"/foodIcons/Allergen-Friendly.png\" alt = \"Allergen-Friendly Icon\" class = \"food-icon\" title = \"Allergen-Friendly item\" style = \"width:3.6vw\">"
            break;

            default:
                return mealtype + ", ";
            break;
        }
    }
    function convertAllergenToIcon(mealtype)
    {
        switch(mealtype)
        {
            case "Eggs":
                return "<img src = \"/foodIcons/Eggs.png\" alt = \"Eggs Icon\" class = \"food-icon\" title = \"Contains Eggs\">"
            break;

            case "Gluten/Wheat":
                return "<img src = \"/foodIcons/Gluten_Wheat.png\" alt = \"Gluten/Wheat Icon\" class = \"food-icon\" title = \"Contains Gluten/Wheat\">"
            break;

            case "Milk":
                return "<img src = \"/foodIcons/Milk.png\" alt = \"Milk Icon\" class = \"food-icon\" title = \"Contains Milk\">"
            break;

            case "Soy":
                return "<img src = \"/foodIcons/Soy.png\" alt = \"Soy Icon\" class = \"food-icon\" title = \"Contains Soy\">"
            break;

            case "Sesame ":
                return "<img src = \"/foodIcons/Sesame.png\" alt = \"Sesame Icon\" class = \"food-icon\" title = \"Contains Sesame\">"
            break;

            case "Fish":
                return "<img src = \"/foodIcons/Fish.png\" alt = \"Fish Icon\" class = \"food-icon\" title = \"Contains Fish\">"
            break;

            case "Shellfish":
                return "<img src = \"/foodIcons/Fish.png\" alt = \"Shellfish Icon\" class = \"food-icon\" title = \"Contains Shellfish\">"
            break;

            case "Pork":
                return "<img src = \"/foodIcons/Pork.png\" alt = \"Pork Icon\" class = \"food-icon\" title = \"Contains Pork\" style = \"width:3.3vw\">"
            break;

            case "Coconut":
                return "<img src = \"/foodIcons/Coconut.png\" alt = \"Coconut Icon\" class = \"food-icon\" title = \"Contains Coconut\" style = \"width:3.3vw\">"
            break;

            case "Peanuts":
                return "<img src = \"/foodIcons/Nuts.png\" alt = \"Peanuts Icon\" class = \"food-icon\" title = \"Contains Peanuts\" style = \"width:3.3vw\">"
            break;

            default:
                return mealtype + ", ";
            break;
        }
    }
    import mealsToday from '../mealsToday.json';
    Object.keys( mealsToday);
    
    let JSONmeals = mealsToday
    let entries = Object.entries(JSONmeals)
    //cafe string will not be sanitized, so this is an issue
    let cafeString = "";
    for (let meal in JSONmeals)
    {
        cafeString += `<div class = "food-meal">${meal}</div>`;
        for (let station in JSONmeals[meal])
        {   
            cafeString += `<div class = "food-station">${JSONmeals[meal][station]["station"]}</div>`;
            for(let menuItemIndex in JSONmeals[meal][station]["menuItems"])
            {
                cafeString += `<div class = "food-item">${JSONmeals[meal][station]["menuItems"][menuItemIndex][0]}</div>`;
                for(let mealType in JSONmeals[meal][station]["menuItems"][menuItemIndex][1][0])
                {
                    //{@html convertMealtypeToIcon("Vegetarian")}
                    //cafeString += JSONmeals[meal][station]["menuItems"][menuItemIndex][1][0][mealType]+ ", ";
                    cafeString += `<div class = "food-mealtype">${convertMealtypeToIcon(JSONmeals[meal][station]["menuItems"][menuItemIndex][1][0][mealType])}</div>`;
                }
                cafeString+="<br>";
                for(let allergen in JSONmeals[meal][station]["menuItems"][menuItemIndex][1][1])
                {
                    //cafeString += JSONmeals[meal][station]["menuItems"][menuItemIndex][1][1][allergen] + ", ";
                    cafeString += `<div class = "food-allergen">${convertAllergenToIcon(JSONmeals[meal][station]["menuItems"][menuItemIndex][1][1][allergen])}`;
                }
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
    

    let src = "/foodIcons/Vegetarian.png"
    //console.log(process.cwd())
</script>

<!--
 

-->
<!-- <img src = {src} alt = "Vegetarian Icon" class = "food-icon" title = "Vegetarian Item"> -->
<!-- {@html string} @html tells it to double check for htmls -->
<!--html does not sanatize string, so if someone else is entering it, then it could break everything: do escape yourself-->

<button onclick = {openAllDetails} type = "button"> Open </button>
<button onclick = {closeAllDetails} type = "button"> Close </button>


<article class = c-wrapper>
    <details open>
        <summary class = "cafe-building">Southside Cafe</summary>
        <div class = "cafe-menu" id= "southside">
            {@html cafeString}

            
        </div>

    </details>
    <details>
        <summary class = "cafe-building">Southside Cafe</summary>
        <div class = "cafe-menu">
            {@html cafeString}
            <!-- {JSON.stringify(mealsToday)} -->
        </div>

    </details>
    <details>
        <summary class = "cafe-building">Southside Cafe</summary>
        <!-- <div class = "cafe-menu">
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

        {/each}        </div> -->
        {@html cafeString}

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
    details :global
    {
        .food-meal
        {
            padding-top: 4vh;
            font-size:3vw;

        }
        
        .food-station
        {
            padding-top: 4vh;
            padding-bottom: 2vh;
            font-size:2.5vw;

        }
        .food-item
        {
            /* padding-top: 2vh; */
            word-wrap: break-word;
            /* font-weight: bold; */
        }
        .food-mealtype
        {
            display:inline;
            white-space: nowrap;
        }
        .food-allergen
        {
            display:inline;
            white-space: nowrap;
        }
        .food-icon
        {
            width: 3vw;
        }
        .food-icon:hover
        {
            filter:grayscale(50%);
        }
    }
    .food-icon
    {
        width: 3vw;
    }
    .food-icon:hover
    {
        filter:grayscale(50%);
    }
    
</style>