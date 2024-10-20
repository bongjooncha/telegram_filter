import { useState, useEffect } from "react";
import style from "./index.module.css";
import { getAllFilter } from "api/filter";

function RunningFilter() {
  const [filterList, setFilterList] = useState([]);

  useEffect(() => {
    const fetchFilterList = async () => {
      const filters = await getAllFilter();
      setFilterList(filters);
    };
    fetchFilterList();
  }, []);

  return (
    <div className={style.RunningFilter}>
      <h1>Running Filter</h1>
      {filterList.map((filter) => (
        <div key={filter.id}>{filter.name}</div>
      ))}
    </div>
  );
}

export default RunningFilter;
