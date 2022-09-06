<template>
    <header>
        <nav>
            <h1>AutoCV</h1>
            <a href="https://github.com/RunItBack1127/autocv-generator" target="_blank" rel="noopener noreferrer">
                <div>
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-github" viewBox="0 0 16 16">
                        <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.012 8.012 0 0 0 16 8c0-4.42-3.58-8-8-8z"/>
                    </svg>
                    <p>Source On GitHub</p>
                </div>
            </a>
        </nav>
    </header>
</template>

<style lang="scss" scoped>
header {
    width: 100%;
    height: 120px;
    display: flex;
    justify-content: center;
    align-items: center;
    box-shadow: rgba(50, 50, 93, 0.25) 0px 2px 5px -1px, rgba(0, 0, 0, 0.3) 0px 1px 3px -1px;

    nav {
        width: 80%;
        height: 100%;
        display: flex;
        justify-content: space-between;
        align-items: center;

        h1 {
            font-weight: 100;
            font-size: 3rem;
            letter-spacing: 0.75rem;
            text-transform: uppercase;
        }

        a {
            width: 350px;
            padding: 25px 0;
            background: #222;
            border-radius: 20px;

            div {
                display: flex;
                justify-content: center;
                align-items: center;
                width: 100%;

                svg {
                    width: 20px;
                    height: 20px;
                    fill: #fff;
                    margin-right: 30px;
                }

                p {
                    font-size: 1.25rem;
                    color: #fff;
                }
            }
        }
    }
}
</style>