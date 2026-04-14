//Mejora propuesta para la función del ejercicio 1

Lista = [1,2,3,4,5];

function getElement(arr, index){
    if(!Array.isArray(arr))
        {
            throw new Error("La lista dada, no es un array")
        }
    
    if(index < 0 || index >= arr.length)
        {
            throw new Error("El indice dado es invalido")
        }
        
    return arr[index]
    }

console.log(getElement(Lista, 10));
console.log(getElement(Lista, 0));
console.log(getElement(Lista, 0)+getElement(Lista, 3));