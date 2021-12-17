<script>
    import UnitCard from "../components/cards/unit_card.svelte";
    import { fade } from 'svelte/transition';
    import { sendQuery } from "../helpers/fakeQuery"

    export let units = [
        {
            device_id: "001",
            EC: 0.250,
            pH: 6.5,
            temperature: 20.15,
            lastUpdate: "2021-12-12 20:00"
        },
        {
            device_id: "002",
            EC: 0.243,
            pH: 6.7,
            temperature: 21.15,
            lastUpdate: "2021-12-12 20:00"
        },
        {
            device_id: "003",
            EC: 0.250,
            pH: 6.5,
            temperature: 20.15,
            lastUpdate: "2021-12-12 20:00"
        },
        {
            device_id: "004",
            EC: 0.243,
            pH: 6.7,
            temperature: 21.15,
            lastUpdate: "2021-12-12 20:00"
        },
    ]

    const get_data = () => {
        const qString = "query Test{Pressure OusideTemperature CloudCoverage pH EC WaterTemperature}"
        // let data = await sendQuery(qString).then(resp => resp.data)
        let data = sendQuery(qString).data
        console.log(data)
        return data
    }

    let selected = undefined;

    const getDevice = (e, unit) => {
        console.log(unit)
        selected = unit;
    }

    // let data = get_data()


</script>

{#if selected}
    <div class="background-container" on:mousedown={e => {
        e.stopPropagation()
        e.preventDefault()
        }} transition:fade>
        <div class="modal-container">
            <img src="static\cancel_black_24dp.svg" alt="close" on:click={e => selected = undefined}>
            <!-- {#await get_data then data} -->
                <UnitCard {...selected} data={get_data()} />
            <!-- {/await} -->
        </div>
    </div>
{/if}
<main class="grid">
    <h1>Units</h1>
    
    <table>
        <thead>
            <th>Device ID</th>
            <th>EC</th>
            <th>pH</th>
            <th>Temperature</th>
            <th>Last Updated</th>
        </thead>
        {#each units as unit}
            <tr on:click={e => getDevice(e, unit)}>
                <td>{unit.device_id}</td>
                <td>{unit.EC} mS/cm3</td>
                <td>{unit.pH}</td>
                <td>{unit.temperature} C</td>
                <td>{unit.lastUpdate}</td>
            </tr>
        {/each}
    </table>

</main>


<style>

    tr {
        transition: 250ms ease-in-out;
        cursor: pointer;
    }

    tr:hover {
        transform: scale(1.02);
        background-color: rgb(185, 208, 241);
    }

    .background-container {
        position:absolute;
        top: 0;
        bottom: 0;
        left: 0;
        right: 0;
        background-color: rgba(0,0,0,0.4);
        z-index: 200;

        display: flex;
        justify-content: center;
        align-items: center;
    }

    .modal-container {
        position: relative;
        background-color: var(--bg-light);
        border-radius: var(--border-radius);
        box-shadow: var(--box-shadow);
    }

    img {
        position: absolute;
        right: 1em;
        top: 1em;
        height: 1.5em;
        cursor: pointer;
        transition: 500ms ease-out;
    }

    img:hover {
        transform: scale(1.05)
    }

</style>