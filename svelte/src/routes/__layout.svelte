<script>

    import Footer from '../components/layout/footer.svelte';
    import Nav from '../components/layout/nav.svelte';
    import Pagetransition from '../components/layout/pagetransition.svelte';

    export let key;

</script>

<!-- 1. Assign current route's path to `key` prop -->
<script context="module">
    export const load = async ({ page }) => ({
      props: {
        key: page.path,
      },
    })
  </script>

<Nav {key} />
<Pagetransition refresh={key}>
    <hr>
    <slot />
</Pagetransition>
<Footer />


<style>

    hr {
        color: transparent;
        margin-bottom: 4em;
    }

</style>