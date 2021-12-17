<script>

    export let title = "Sow seeds of famine"
    export let body = "Get rid of those silly little plants and make them pay for eating your lunch that one time"
    export let person = {
        name: undefined,
        src:undefined,
    }
    export let buttonText
    export let buttonClick
    export let unit

</script>


<div class="container">
    <h3>{title}</h3>
    {#if person && person.name}
        <h4>{person.name}</h4>
    {/if}
    <p>{body}</p>
    <button on:click={e => buttonClick(e, unit)}>{buttonText}</button>
</div>


<style>

    .container {
        border-radius: .5em;
        padding: 1em 2em;
        box-shadow: var(--box-shadow);
        margin-bottom: 1.5em;
        margin-right: 2em;
        transition: 250ms ease-out;
    }

    .container:hover {
        transform: scale(1.05);
    }

    .wrap {
        display:flex;
        align-items: center;
    }


    h3 {
        font-size: 1.5em;
        font-weight: var(--font-heavy);
    }
    
    h4 {
        font-size: 1.2em;
        font-weight: var(--font-light);
        
    }

    img {
        object-fit: contain;
        height: 1.5em;
        width: 1.5em;
        border-radius: 50%;
        background-color: tomato;
        margin-right: 1em
    }

    button {
        color: white !important;
        background-color: var(--bg-card);
        box-shadow: none;
        outline:none !important;
        border-radius: var(--border-radius);
        padding: .5em;
        margin-top: 1em;
        justify-self: center;
        cursor: pointer;
        color: var(--txt-mid);
        font-weight: var(--font-heavy);
    }
    
    button:focus {
        color: var(--txt-light);

    }

</style>