<footer>
    <!-- <span class="footer">Find Me On:</span> -->
    <!-- <div class="social-icons">
        <img class="social-icon" src="src/images/socials/linkedin.svg" alt="">
        <img class="social-icon invert" src="src/images/socials/github.svg" alt="">
        <img class="social-icon invert" src="src/images/socials/email.svg" alt="">
    </div> -->
    <span class="footer copyright">Copyright Chris Vail 2021</span>
</footer>

<style>

footer {
        display: flex;
        flex-direction: column;
        align-items: center;
        background-color: var(--bg-darker);
        padding: 2em;
        margin-top: 5em;
    }

    footer > * + *{
        margin-top: 1em;
    }

    .footer {
        color: var(--txt-light);
        font-family: Roboto, sans-serif;
        font-size: 1.25em;
    }

    .copyright {
        font-size: .75em;
        opacity: 50%;
    }

    .social-icons {
        width: 15vw;
        display: flex;
        justify-content: space-between;
    }

    .social-icon {
        height: 3em;
        filter: saturate(70%);
        cursor: pointer;
        transition: transform 250ms ease;
    }

    .social-icon:hover {
        transform: scale(1.05);
    }

    .invert {
        filter: invert()
    }

    
</style>