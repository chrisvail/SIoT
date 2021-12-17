const endpoint =  import.meta.env.VITE_GRAPHQL_ENDPOINT
const headers = {
    'Accept': 'application/json',
    "Content-Type": "application/json",
    "x-api-key":import.meta.env.VITE_GRAPHQL_API_KEY
};


export const sendQuery = async (queryString, queryVars) => {
    let query;
    if (queryVars) {
        query = JSON.stringify({
            query: queryString,
            variables: queryVars
        })
    } else {
        query = JSON.stringify({
            query: queryString
        })
    }
    
    const result = await fetch(endpoint, {
        method:"POST",
        headers,
        body:query
    })
    .then(response => response.json())

    return result;
}