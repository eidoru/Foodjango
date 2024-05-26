const NavigationRoutes = {
  patron: [
    { name: "Dashboard", route: "/" },
    { name: "Restaurants", route: "/restaurants" },
    { name: "Carts", route: "/carts" },
    { name: "Orders", route: "/orders" },
  ],
  vendor: [
    { name: "Dashboard", route: "/" },
    { name: "Manage Restaurants", route: "/manage-restaurants" },
  ],
  runner: [
    { name: "Dashboard", route: "/" },
    { name: "Manage Orders", route: "/manage-orders" },
  ],
};

export { NavigationRoutes };
