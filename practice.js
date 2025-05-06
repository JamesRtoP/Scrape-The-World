function sumLength(...strings)//rest argument
{
    let sum = 0;
    for (let string of strings)
    {
        sum += string.length
    }
    return sum;
}

function myCat(...strings)//rest argument
{
    let newStr = "";
    for (let string of strings)
    {
        newStr += string +=" ";
    }
    return newStr;
}


fourOFive = [4,0,5];
function headingBackTo (one,two,three)
{
    console.log("I'm heading back to",one,two,three)
}
//curried headingBackTo as well as used put in fourOFive elements into the functions individually
let ofCorset = function ()
{ 
    headingBackTo(...fourOFive);
}   //ofCorset
//console.log(myCat("I'm","an","ass","boy"))

function randomFromXXToXX (from, too)
{
    return Math.floor(from +(Math.random()*(too-from + 1)))
}
let oneToTen = () => randomFromXXToXX(1,10);

let arrrrrrr = [];
for (i = 0;i<50; i++)
{
    arrrrrrr.unshift(oneToTen());
}

//console.log(arr)


//Destructuring
//or automatically getting indexes as arguments in a function
let xyz1= [1,2,3];
let xyz2= [4,4,4]
function distanceBetweenTwoPoints([x1,y1,z1],[x2,y2,z2])
{
    return Math.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)
}
//console.log(distanceBetweenTwoPoints(xyz1, xyz2))


//destructuring for objects
biofile = {phoneNumber: "(425)931-5667", age :45};
let {phoneNumber} = biofile
//console.log(phoneNumber);


//optional property access
//.? operator
//works if it is defined
//returns undefined if the property doesn't exist
//works for square brackets, somehow, idk man


let sumch = (arr)=>
{
    let sum = 0;
    for(let i = 0; i < arr.length; i++)
    {
        sum += arr?.[i];
    }
    return sum;
}
let rangech = (from, too, step = start < end ? 1 : -1) =>
{
   
    let arr = [];
    if(step > 0)
    {
        for(let i = from; i<= too; i +=step)
        {
            arr.push(i);
        }
    }
    else
    {
        for(let i = from; i>= too; i +=step)
        {
            arr.push(i);
        }
    }
    return arr;
}

//console.log(sumch(rangech(1,10)))


let reverseArray = (arr) =>
{
    let returnArray = [];
    for (element of arr)
    {
        returnArray.unshift(element);
    }
    return returnArray;

}

let reverseArrayInPlace = (arr) =>
{
    for(let firstIndex = 0, secondIndex = arr.length; firstIndex < secondIndex; firstIndex++, secondIndex++)
    {
        let temp = arr[firstIndex];
        arr[firstIndex] = arr[secondIndex]; //no pointers but 
        arr[secondIndex] = temp;
    }
}


//let arr = [1,2,3,4,5];
//console.log(reverseArray(arr));
//console.log(arr)
//console.log(arr);


let arrayToList = (array) =>
{
    let list = {};
    let curList = list
    for (element of array)
    {
        curList.value = element;
        curList.next = {};
        curList = curList.next;
    }
    return list;
}

let theirArrayToList = (array) =>
{
    let list = {};
    for (element of array)
    {
        list = {value:elemnt, next:list}
    }
    return list;
}


//arr = [1,2,3,4,5]
//console.log(arrayToList(arr))

let listToArray = (list) =>
{
    arr = [];
    let curList = list;
    while(Object.keys(curList).length > 0)
    {
        arr.push(curList.value);
        curList = curList.next
    }
    
    return arr;
}

//works ish, adds an undefined
let thierListToArray = (list) => 
{
    arr = [];
    let curList = list;
    while(curList)
    {
        arr.push(curList.value);
        curList = curList.next
    }
    
    return arr;
}
//arr = [1,2,3,4,5];
//console.log(thierListToArray(arrayToList(arr)));

let prepend = (obj, list) =>//insert at front
{
    return {value: obj, next:list}
}

//console.debug(prepend(10, prepend(20, null)));
//console.debug( prepend(20, null));

let nth = (list, n) =>
{
    curList = list;
    for(;n > 0 && curList;n--)
    {
        curList = curList.next;
    }
    return !curList ? undefined : curList.value;
}

//arr = [1,2,3,4,5];
//console.log(nth(arrayToList(arr),8));



let printRelationship = (x,y,z=x<y?" is less than ": " is greater than ") =>
{
    console.log(x + z + y);
}

//printRelationship(7,5)


let deepComparison = (x,y) => //fucks up on some cases, particularly strings
{
    let equal = true;
    let xKeys = Object.keys(x);
    let yKeys = Object.keys(y);
    if (xKeys.length == yKeys.length)
    {
        if(xKeys.length == 0)
        {
            equal = x == y;
        }
        else if(xKeys.length = 1 && xKeys[0] == yKeys[0] && x[xKeys[i]] == y[xKeys[i]])
        {
            
        }
        else
        {
            for(let i = 0; i < xKeys.length; i++)
            {
                if(xKeys[i] != yKeys[i] || !deepComparison(x[xKeys[i]], y[xKeys[i]]))
                {   
                    equal = false;
                }
            }
        }
    }
    else
    {
        equal = false;
    }
    return equal;
}
/*
let x = [0,5,6,6];
let y = [0,5,6,6];

let xx = 88;
let yy = 8;

let xxx = {ass:98, y:x}
let yyy = {ass:98, y}

let xy = "ass"

//console.log(    (   x[  Object.keys(x)[0]   ]  )    )
//console.log(xx == yy)
//console.log(deepComparison(xxx,yyy))
//console.log(yyy)

//console.log(Object.keys(xy))

let obj = {here: {is: "an"}, object: 2};
console.log(deepComparison(obj, obj));
// → true
console.log(deepComparison(obj, {here: 1, object: 2}));
// → false
console.log(deepComparison(obj, {here: {is: "an"}, object: 2}));
// → true

*/

let x = null;
let y = null;
let theirDeepCompare = (a,b) =>
{
    if(a===b)
    {
        return true;
    }
    if(a == null || typeof a != "object" || b == null || typeof b != "object")
    {
        return false;
    }
    let keysA = Object.keys(a), keysB = Object.keys(b);

    if (keysA.length != keysB.length) return false;

    for (let key of keysA) 
    {
        if (!keysB.includes(key) || !theirDeepCompare(a[key], b[key])) 
        {        
            return false;
        }
    }

  return true;
}
//console.log( theirDeepCompare(x,y));
while(false)
{
    
}

















































//curry rotation matrix for each angle