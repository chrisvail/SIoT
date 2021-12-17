<script>

    export let key;
    
</script>

<header class="nav-grid">
    <a class="logo" href="/">HydroFarm v0.1</a>
    <nav>
        <a href="/" class="nav-item {'/' === key ? 'current-page' : ''}">Home</a>
        <a href="/tasks" class="nav-item {'/tasks' === key ? 'current-page' : ''}">Tasks</a>
        <a href="/units" class="nav-item {'units' === key.split('/')[1] ? 'current-page' : ''}">Units</a>
        <a href="/analysis" class="nav-item {'analysis' === key.split('/')[1] ? 'current-page' : ''}">Analysis</a>
    </nav>
</header>

<style>

    header {
        position: fixed;
        top: 0;
        z-index: 100;
        background-color: var(--bg-card);
        /* backdrop-filter: saturate(180%) blur(20px); */
        width: var(--nav_width);
        height: 100%;
        padding: 1em 0 1em;
        text-align: right;
        z-index: 100;
    }
    
    .logo {
        grid-column: content-start / 5;
        color: var(--txt-light);
        font-weight: 700;
        cursor: pointer;
        font-size: 2em;
        padding: .2em 1em;
        margin-bottom: 3em;
    }
    
    nav {
        grid-column: 8 / content-end;
        display: flex;
        flex-direction: column;
        justify-content: start;
        align-items: left;
        width: 100%;
        padding: 5em 0;
    }
    
    .nav-item {
        color: #8d9fbb;
        background-color: var(--bg-card);
        text-decoration: none;
        font-family: Roboto;
        font-weight: var(--font-heavy);
        font-size: 1.25em;
        position: relative;
        /* padding: .25em 0em; */
        /* border-top: 0.5px solid var(--bg-darker);
        border-bottom: 0.5px solid var(--bg-darker); */
        /* box-shadow: ; */
        padding: 1em;
    }

    /* .nav-item::after {
        content: "";
        position: absolute;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 3px;
        background-color: rgb(240, 158, 36);
        transform-origin: right;
        transform: scaleX(0);
        transition: transform 250ms ease-out;
    }
    
    .nav-item:hover::after {
        transform: scaleX(1);
        transform-origin: left;
    } */

    .nav-item:hover{
        color: var(--txt-light);
        transform: scale(1.05);
        box-shadow: var(--box-shadow);

    }

    .current-page {
        background-color: hsl(215, 78%, 14%);
        color: var(--txt-light);
    }

</style>