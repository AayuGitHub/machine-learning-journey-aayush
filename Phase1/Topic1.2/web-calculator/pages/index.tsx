import Head from 'next/head';
import Calculator from '../components/Calculator';
import ThemeToggle from '../components/ThemeToggle';

export default function Home() {
    return (
        <>
            <Head>
                <title>Scientific Calculator</title>
                <meta name="viewport" content="width=device-width, initial-scale=1" />
            </Head>
            <ThemeToggle />
            <main className="flex min-h-screen flex-col items-center justify-center p-4 transition-colors duration-500">
                <div className="z-10 w-full max-w-5xl items-center justify-center font-sans text-sm lg:flex mb-12">
                    <h1 className="text-4xl font-extralight text-slate-800 dark:text-white/80 tracking-[0.2em] uppercase drop-shadow-sm">Calculator</h1>
                </div>

                <Calculator />

                <div className="mt-12 text-slate-500 dark:text-white/30 text-xs font-medium tracking-wider uppercase">
                    Designed with Premium Glassmorphism
                </div>
            </main>
        </>
    )
}
