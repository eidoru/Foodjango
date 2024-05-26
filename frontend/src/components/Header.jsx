import PropTypes from "prop-types";

function Header({ activeButton }) {
  Header.propTypes = {
    activeButton: PropTypes.string.isRequired,
  };

  return (
    <div className="h-[84px] p-6 text-3xl font-bold shadow-sm">
      {activeButton}
    </div>
  );
}

export default Header;
