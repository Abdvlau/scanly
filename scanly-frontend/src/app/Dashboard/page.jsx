"use client"
import React, { useState } from 'react';
import Footer from './Footer'; // Assuming Footer is in the same directory

const DashboardPage = () => {
    const [selectedCourse, setSelectedCourse] = useState('');
    const [selectedDate, setSelectedDate] = useState('');
    const [selectedDepartment, setSelectedDepartment] = useState('');

    const handleCourseChange = (event) => {
        setSelectedCourse(event.target.value);
    };

    const handleDateChange = (event) => {
        setSelectedDate(event.target.value);
    };

    const handleDepartmentChange = (event) => {
        setSelectedDepartment(event.target.value);
    };

    const generateQRCode = () => {
        // Implement QR code generation logic here
    };

    return (
        <div className='bg-[#ffffff19] space-x-4'>
            <div className="text-center">
                <h1 className="lg:text-4xl md:mb-0 flex justify-center text-2xl font-bold mb-4">
                    <span className="italic text-gray-400">Welcome</span><span className="ml-1 text-gray-400 ">To the Student Dashboard</span>
                </h1>
            </div>
            <div className="flex justify-between items-center space-x-4">
                <div className="mb-4">
                    <label htmlFor="course" className="mr-2 text-gray-400">Select Course:</label>
                    <select id="course" value={selectedCourse} onChange={handleCourseChange} className="border border-gray-300 rounded p-2 bg-blue-950 text-gray-400">
                        <option value="">-- Select Course --</option>
                        <option value="microeconomics">Microeconomics</option>
                        <option value="macroeconomics">Macroeconomics</option>
                        <option value="econometrics">Econometrics</option>
                        {/* Add more courses as needed */}
                    </select>
                </div>

                <div className="mb-4">
                    <label htmlFor="date" className="mr-2 text-gray-400">Select Date:</label>
                    <input type="date" id="date" value={selectedDate} onChange={handleDateChange} className="border border-gray-300 rounded p-2" />
                </div>

                <div className="mb-4">
                    <label htmlFor="department" className="mr-2 text-gray-400">Select Department:</label>
                    <select id="department" value={selectedDepartment} onChange={handleDepartmentChange} className="border border-gray-300 rounded p-2 bg-blue-950 text-gray-400">
                        <option value="">-- Select Department --</option>
                        <option value="cs">Computer Science</option>
                        <option value="it">Information Technology</option>
                        <option value="se">Software Engineering</option>
                        {/* Add more departments as needed */}
                    </select>
                </div>

                <button onClick={generateQRCode} className="text-gray-400 hover:bg-gray-400 hover:text-black bg-blue-950 rounded-lg p-2 duration-900 px-5 py-2.5 md:w-auto w-full">Generate QR Code</button>
            </div>
            <Footer />
        </div>
    );
}

export default DashboardPage;
