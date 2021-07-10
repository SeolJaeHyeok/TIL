import React from "react";

export default ({ name, children }) => (
  <>
    <h2>{name}</h2>
    <ul>{children}</ul>
  </>
);
