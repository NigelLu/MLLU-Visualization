# region Setup
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# endregion


def drawline(data, do_melt=True, hue=None, id_vars=['Tuning Method', "Dataset"], x_label="X_label", y_label='Objective', markers=True, dashes=False, save_config=[False, None], facet_grid_config={"col": "Dataset", "row": None}):
    """
        Takes in a set of arguments
        Draws/Saves the visualized lineplot using seaborn

            Parameters:
                data (pandas.DataFrame): A pandas DataFrame to store all the necessary data for plotting
                do_melt (boolean): Optional boolean argument for specifiying whether to melt the dataset according to id_vars, default to True
                hue (str): Optional string argument for specifying what column should be used for hue if do_melt is False
                id_vars (list): A list of strings specifying which columns to retain when melting
                x_label (str): Optional string argument for specifying the label of X-axis, default to 'X_label'
                y_label (str): Optional string argument for specifying the label of Y-axis, default to 'Objective'
                markers (boolean): Optional boolean argument for specifiying whether to use markers for points on the lineplot, default to True
                dashes (boolean): Optional boolean argument for specifiying whether to use dashes in the lineplot, default to False. 
                save_config (list): Optional save configuration argument for specifying whether and how to store the image. Take a list of two variables, first being boolean, second being string (to specify save directory)


            Returns:
                None
    """

    assert type(data) == pd.DataFrame
    assert (save_config[0] and type(save_config[1])
            == str) or (not save_config[0])

    df = data
    if do_melt:
        df = pd.melt(data, id_vars=id_vars, var_name=x_label)

    g = sns.FacetGrid(df, col=facet_grid_config['col'], row=facet_grid_config["row"],
                      sharey=False, sharex=False, height=6, aspect=0.9)
    g = g.map_dataframe(sns.lineplot, x=x_label, y="value" if do_melt else y_label,
                        hue=hue if hue else id_vars[0], markers=markers, dashes=dashes, style=id_vars[0] if markers else None)
    g.set_axis_labels(x_var=x_label, y_var=y_label)

    # add legends to graphs
    for ax in g.axes.ravel():
        ax.legend()

    # linePlot = sns.lineplot(x=x_label, y='value', data=melted_df, hue=id_vars[0], markers=markers, dashes=dashes, style=id_vars[0] if markers else None)
    # linePlot.set_xlabel(x_label)
    # linePlot.set_ylabel(y_label)

    if (save_config[0]):
        g.savefig(save_config[1])
    else:
        plt.show()
