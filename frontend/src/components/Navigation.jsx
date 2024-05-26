import axios from "axios";

import PropTypes from "prop-types";
import LogOut from "../icons/LogOut";

import { useAuth } from "../hooks/useAuth";
import { useEffect, useState } from "react";

import { Link } from "react-router-dom";
import { NavigationRoutes } from "../navroutes";

function Navigation({ activeButton, setActiveButton }) {
  const [user, setUser] = useState({});
  const { token, setToken } = useAuth();

  useEffect(() => {
    if (token === null || token === "null") return;
    axios
      .get("http://localhost:8000/api/me/", {
        headers: { Authorization: `Token ${token}` },
      })
      .then((response) => {
        setUser(response.data);
        console.log(response.data);
      });
  }, [token]);

  const buttons = user.role ? NavigationRoutes[user.role] : [];

  return (
    <div className="flex h-16 items-center justify-between bg-green-600 p-3.5">
      <div className="flex space-x-4">
        {buttons.map((button) => (
          <Link
            key={button.name}
            to={button.route}
            onClick={() => setActiveButton(button.name)}
            className={`rounded-md px-3 py-2 text-sm font-medium transition hover:bg-green-700 hover:text-white ${
              button.name === activeButton
                ? "bg-green-700 text-white"
                : "text-gray-300"
            }`}
          >
            {button.name}
          </Link>
        ))}
      </div>
      <div className="flex items-center space-x-4">
        <p className="text-sm font-medium text-white">{`${user.first_name} ${user.last_name}`}</p>
        <button
          type="button"
          className="rounded-md p-2 text-gray-300 transition hover:bg-green-700 hover:text-white"
          onClick={() => setToken(null)}
        >
          <LogOut className="size-4" strokeWidth="2.5" />
        </button>
      </div>
    </div>
  );
}

Navigation.propTypes = {
  activeButton: PropTypes.string.isRequired,
  setActiveButton: PropTypes.func.isRequired,
};

export default Navigation;
