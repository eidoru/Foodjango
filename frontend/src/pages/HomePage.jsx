import { useState } from "react";

import PropTypes from "prop-types";

import Navigation from "../components/Navigation";
import Header from "../components/Header";
import { Outlet } from "react-router-dom";

function HomePage() {
  const [activeButton, setActiveButton] = useState("Dashboard");

  HomePage.propTypes = {
    setPage: PropTypes.func.isRequired,
  };

  return (
    <>
      <Navigation
        activeButton={activeButton}
        setActiveButton={setActiveButton}
      />
      <Header activeButton={activeButton} />
      <div className="p-10">
        <Outlet />
      </div>
    </>
  );
}

export default HomePage;
