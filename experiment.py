import utils
import decoder
import data_generator as dg

def exp_gbrbm(exp_name, T=[]):
    dataset = dg.one_exception_dataset(
        N=6,
        n=1500,
        T=T,
        lam=5000,
        exc=1,
        noise_k=1
    )
    utils.write_data(dataset, exp_name, "generated_data")
    new_data = utils.tsne(dataset, exp_name, "generated_data", T, 2)
    utils.write_data(new_data, exp_name, "generated_data_for_tsne")

    _, recovery_sample, decode_res = decoder.gbrbm_decoder(
        dataset,
        learning_rate=0.1,
        training_epochs=50,
        batch_size=1001,
        n_hidden=2000,
        plot_every=1
    )
    utils.write_data(decode_res, exp_name, "decoded_data")
    new_data = utils.tsne(decode_res, exp_name, "decoded_data", T, 2)
    utils.write_data(new_data, exp_name, "decoded_tsne_data_for_tsne")

if __name__ == "__main__":
    exp_gbrbm("N6_n1500_t5_e1_gbrbm_h2000_2D", T=[0, 1, 2, 3, 4, 5])
