<script>

    import Gauge from "../charts/gauge.svelte"
    import Linegraph from "../charts/linegraph.svelte";

    

    export let device_id;
    export let EC
    export let pH
    export let temperature
    export let lastUpdate
    export let data


    const getComment = (name, val, ref) => {
        if (val > ref*1.1) {
            return `Your ${name} is getting a little high`
        } else if (val < ref * 0.9) {
            return `Your ${name} is getting a little low`
        } else {
            return "This is looking just right to us"
        }
    }

    let current_page = "home"

    const getHistory = (variable) => {
        if (variable === "EC") {
            let keys = Object.keys(data.EC).sort()
            keys = keys.slice(-300, -1)

            let values = []
            labels = []
            for (let i = 0; i < keys.length; i++) {
                values.push(data.EC[keys[i]])
                console.log(data.EC[keys[i]])
                labels.push(keys[i])
            }

            console.log(keys)
            return values
            

        } else if (variable === "pH") {

            // console.log("DATA: " + JSON.stringify(data.EC))
            let keys = Object.keys(data.pH).sort()
            keys = keys.slice(-300, -1)

            let values = []
            labels = []
            for (let i = 0; i < keys.length; i++) {
                values.push(data.pH[keys[i]])
                console.log(data.pH[keys[i]])
                labels.push(keys[i])
            }

            console.log(keys)
            return values
            
        } else if (variable === "temperature") {
            // console.log("DATA: " + JSON.stringify(data.EC))
            let keys = Object.keys(data["Water Temperature"]).sort()
            keys = keys.slice(-300, -1)

            let values = []
            labels = []
            for (let i = 0; i < keys.length; i++) {
                values.push(data["Water Temperature"][keys[i]])
                console.log(data["Water Temperature"][keys[i]])
                labels.push(keys[i])
            }

            console.log(keys)
            return values
        }
    }
    let labels = "1 2 3 4 5 6 7 8 9 10".split(" ")

</script>


<div class="container">
    <h3>Device {device_id}</h3>
    {#if current_page === "home"}
        <div class="gauge">
            <Gauge title="EC" value={EC} reference=0.200 range={[0, 0.4]} comment={getComment("EC", EC, 0.2)} style="margin: 0 auto 1em"/>
            <button on:click={e => current_page = "EC"}>See History</button>
        </div>
        <div class="gauge">
            <Gauge title="pH" value={pH} reference=6.5 range={[0, 14]} comment={getComment("pH", pH, 6.5)} style="margin: 0 auto 1em"/>
            <button on:click={e => current_page = "pH"}>See History</button>
        </div>
        <div class="gauge">
            <Gauge title="Temperature" value={temperature} reference=22 range={[0, 50]} comment={getComment("Temperature", temperature, 22)} style="margin: 0 auto 1em"/>
            <button on:click={e => current_page = "temperature"}>See History</button>
        </div>
    {:else if current_page === "EC"}
        <div class="line-wrap">
            <Linegraph label="EC over time" data={getHistory("EC")} labels={labels} beginZero={false} style="grid-column: span 2"/>
            <button class="back" on:click={e => current_page = "home"}>Back</button>
        </div>
    {:else if current_page === "pH"}
        <div class="line-wrap">
            <Linegraph label="pH over time" data={getHistory("pH")} labels={labels} beginZero={false} style="grid-column: span 2"/>
            <button class="back" on:click={e => current_page = "home"}>Back</button>
        </div>
    {:else if current_page === "temperature"}
        <div class="line-wrap">
            <Linegraph label="Temperature over time" data={getHistory("temperature")} labels={labels} beginZero={false} style="grid-column: span 2"/>
            <button class="back" on:click={e => current_page = "home"}>Back</button>
        </div>
    {/if}
    <p class="update">Last updated: {lastUpdate}</p>
</div>


<style>

    .container {
        padding: 2em;
        display: grid;
        gap: 0.5em;
        min-width: 50em;
    }

    h3 {
        grid-column: span 2;
    }

    p.update {
        color: var(--txt-mid);
        font-style: italic;
        font-size: 0.8em;
        grid-column: span 2;
        justify-self: center;
    }

    .gauge {
        display: flex;
        flex-direction: column;
    }

    button {
        background-color: transparent;
        border: none;
        justify-self: center;
        margin-top: -1.25em;
        cursor: pointer;
        color: var(--txt-mid);
        font-weight: var(--font-heavy);
    }
    
    .back {
        justify-self: right;
        margin-top: 0em;
        grid-column: 2/3;
        font-size: 1em;
        transition: 500ms ease-out;
    }

    .back:hover {
        transform: scale(1.05);
    }

</style>