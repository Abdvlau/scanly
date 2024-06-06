"use client"
import Link from 'next/link';

const StaffSignUpPage = () => {
    return (
        <main className="bg-white min-h-screen flex items-center justify-center">
            <div className="w-full max-w-md">
                <aside className="bg-white rounded-xl shadow-lg p-8">
                    <h1 className="text-center text-black font-light text-4xl bg-yellow rounded-t-xl m-0 py-4">Staff Register</h1>
                    <form action="">
                        <input type="text" name="Firstname" placeholder="Firstname" className="w-full p-2 mb-4 border rounded" />
                        <input type="text" name="Surename" placeholder="Surename" className="w-full p-2 mb-4 border rounded" />
                        <input type="email" name="email" placeholder="Email" className="w-full p-2 mb-4 border rounded" />
                        <input type="text" name="department" placeholder="Department" className="w-full p-2 mb-4 border rounded" />
                        <input type="text" name="position" placeholder="Position" className="w-full p-2 mb-4 border rounded" />
                        <div className="flex justify-between items-center">
                            <Link href="/signup" legacyBehavior>
                                <a className="text-blue-900">Already registered?</a>
                            </Link>
                            <button type="submit" className="bg-blue-900 text-white rounded p-2">Register</button>
                        </div>
                    </form>
                </aside>
            </div>
        </main>
    );
};

export default StaffSignUpPage;