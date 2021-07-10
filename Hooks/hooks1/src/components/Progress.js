import React from "react";
import { useState } from "../context";
import styled from "@emotion/styled";

const ProgressBar = styled.section`
  margin-bottom: 20px;
`;

const Bar = styled.div`
  display: flex;
  align-items: center;
  & > *:not(:last-child) {
    margin-right: 20px;
  }
  span {
    font-size: 20px;
  }
`;

const P = styled.p`
  text-align: center;
  margin: 0;
  font-size: 18px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.5px;
`;
export default () => {
  const { toDos, completed } = useState();
  const percent = Math.floor(
    (completed.length / (toDos.length + completed.length)) * 100
  );

  return (
    <>
      {!isNaN(percent) && (
        <ProgressBar>
          <P>{toDos.length} more to go!</P>
          <Bar>
            <label htmlFor="progress">
              <span role="img" aria-label="Waxing Gibbous Moon">
                🌔
              </span>
            </label>
            <progress id="progress" max="100" value={percent}></progress>
            <span role="img" aria-label="full moon">
              🌕
            </span>
          </Bar>
        </ProgressBar>
      )}
    </>
  );
};
